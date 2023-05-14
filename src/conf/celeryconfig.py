broker_url = "amqp://guest:guest@localhost:5672//"

result_backend = "db+sqlite:///celery-results.db"

task_track_started = True

worker_cancel_long_running_tasks_on_connection_loss = True

broker_pool_limit = 1
broker_heartbeat = None
task_acks_late = True
worker_prefetch_multiplier = 1

# TODO: Add routes
task_routes = {
    "src.celery_worker.forward_wall": {"queue": "vtt-wall"},
}
