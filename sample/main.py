import _jsonnet
import json
import random

# --- Files ---
USER_KEY_FILE = 'user_key.json'
USER_ID_FILE = 'user_id.json'
ITEM_IDS_FILE = 'item_ids.json'
JSONNET_FILE = 'template.jsonnet'  # Assuming your Jsonnet file is named this

# Load data from JSON files
try:
    with open(USER_KEY_FILE, 'r') as f:
        user_key_data = json.load(f)
    with open(USER_ID_FILE, 'r') as f:
        user_id_data = json.load(f)
    with open(ITEM_IDS_FILE, 'r') as f:
        item_ids_data = json.load(f)
except FileNotFoundError as e:
    print(f"Error: Could not find input file {e.filename}")
    exit(1)
except json.JSONDecodeError as e:
    print(f"Error: Could not parse JSON in file. Details: {e}")
    exit(1)

four_rand_items = random.sample(item_ids_data, 4)
one_user_key = random.choice(user_key_data)
one_user_id = random.choice(user_id_data)

num_of_requests = 5  # Number of requests to generate
print(f"\n--- Generating {num_of_requests} random requests ---")
all_requests_data = []

for i in range(5):
    # Generate new random values for each request
    ext_vars_loop = {
        "user_key": json.dumps(one_user_key),
        "user_id": json.dumps(one_user_id),
        "item_ids": json.dumps(four_rand_items),
    }
    try:
        jstr_loop = _jsonnet.evaluate_file(
            JSONNET_FILE,
            ext_vars=ext_vars_loop
        )
        all_requests_data.append(json.loads(jstr_loop))
    except RuntimeError as e:
        print(f"Jsonnet evaluation error during loop (iteration {i + 1}): {e}")
        # Decide if you want to stop or continue
        break

# Encapsulate into the structure your print statement expected
output_multiple = {"data": all_requests_data}

with open("outputs.json", "w", encoding="utf-8") as f:
    json.dump(output_multiple["data"], f, indent=2, ensure_ascii=False)

print("输出已写入 outputs.json")
