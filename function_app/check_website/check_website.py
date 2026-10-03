import azure.functions as func
from azure.data.tables import TableServiceClient
import requests
import datetime
import os
import logging
 
def main(mytimer: func.TimerRequest) -> None:
    target_url   = os.environ["TARGET_URL"]
    storage_conn = os.environ["AzureWebJobsStorage"]
 
    check_time    = datetime.datetime.now(datetime.timezone.utc)
    result_status = "PASS"
    error_detail  = None
    response_ms   = None
 
    try:
        response    = requests.get(target_url, timeout=10)
        response_ms = response.elapsed.total_seconds() * 1000
 
        if response.status_code != 200:
            result_status = "FAIL"
            error_detail  = f"HTTP {response.status_code}"
 
        elif response_ms > 5000:
            result_status = "SLOW"
            error_detail  = f"Response time {response_ms:.0f}ms exceeded 5000ms"

    except requests.exceptions.ConnectionError:
        result_status = "FAIL"
        error_detail  = "Connection refused — server unreachable"
 
    except requests.exceptions.Timeout:
        result_status = "FAIL"
        error_detail  = "Request timed out after 10 seconds"
 
    except Exception as e:
        result_status = "FAIL"
        error_detail  = str(e)
 
    # ── Write result to Table Storage ────────────────────────────────────
    #
    # IMPORTANT — PartitionKey restrictions:
    # Azure Table Storage does not allow / : # ? in PartitionKey or RowKey.
    # The target URL (https://example.com) contains / and : which cause
    # silent write failures — rows appear to succeed but never show up.
    # Use the hardcoded string "uptime" as the PartitionKey instead.
    #
    # IMPORTANT — Use TableServiceClient, not TableClient:
    # create_table_if_not_exists() is a method on TableServiceClient.
    # TableClient does not have this method and raises AttributeError.
    # Always call create_table_if_not_exists() on the service client,
    # then get the table client separately for entity operations.
    #
 
    entity = {
        # "uptime" instead of target_url — URLs contain / and : which are
        # forbidden characters in Azure Table Storage partition keys.
        "PartitionKey": "uptime",
        "RowKey":       check_time.strftime("%Y%m%d%H%M%S"),
        # "Timestamp" is a reserved system property set by Table Storage.
        "CheckTime":    check_time.isoformat(),
        "Status":       result_status,
        "ResponseMs":   int(response_ms) if response_ms is not None else 0,
        "ErrorDetail":  error_detail or "",
        "TargetUrl":    target_url,
    }
 
    ms_text = f"{response_ms:.0f}ms" if response_ms is not None else "n/a"
    logging.info(f"Check: {result_status} | {ms_text} | {target_url}")

    try:
        table_service = TableServiceClient.from_connection_string(storage_conn)
        table_service.create_table_if_not_exists("uptimechecks")
        table_client  = table_service.get_table_client("uptimechecks")
        table_client.upsert_entity(entity)
    except Exception as e:
        logging.error(f"Failed to write result to table: {e}")
 
    if result_status != "PASS":
        logging.error(f"SITE DOWN: {target_url} | {result_status} | {error_detail}")
