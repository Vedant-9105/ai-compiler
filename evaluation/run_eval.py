import requests, json, time

def evaluate():
    with open("dataset.json") as f:
        dataset = json.load(f)
    metrics = {"success": 0, "retries": [], "latencies": []}
    for item in dataset:
        start = time.time()
        resp = requests.post("http://localhost:8000/generate", json={"prompt": item["prompt"]})
        latency = time.time() - start
        metrics["latencies"].append(latency)
        if resp.status_code == 200 and validate_output(resp.json()):
            metrics["success"] += 1
    print(f"Success rate: {metrics['success']/len(dataset)*100}%")
    print(f"Avg latency: {sum(metrics['latencies'])/len(metrics['latencies'])}s")