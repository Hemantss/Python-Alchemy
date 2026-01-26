import itertools
import random
def user_event_stream():
    while True:
        yield {
            "user_id": random.randint(1000, 9999),
            "action": random.choice(["click", "view", "purchase"])
        }

event_ids = itertools.count(start=1)
variants = itertools.cycle(["A", "B", "C"])
model_version = itertools.repeat("reco_model_v3.2")

events = user_event_stream()

for _ in range(10): # controlled consumption
    event = next(events)
    enriched_event = {
        "event_id": next(event_ids),
        "user_id": event["user_id"],
        "action": event["action"],
        "variant": next(variants),
        "model": next(model_version)
    }
    print(enriched_event)