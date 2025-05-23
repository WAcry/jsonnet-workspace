# Jsonnet Workspace

Samples to use Python with Jsonnet templates to batch-generate structured JSON data.

## Usage

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Run the main script:

```bash
python main.py
```

After running, batch data will be generated in `outputs.json`.

## Example Output

A sample randomly generated object in `outputs.json`:

```json
{
  "user_key": "user_key_1002",
  "user_id": 1002,
  "item_ids": [
    "item_B",
    "item_C"
  ],
  "order_items": [
    {
      "order_id": 2,
      "amount": 10
    },
    {
      "order_id": 4,
      "amount": 20
    }
  ]
}
```

## Data Description

- `item_ids.json`: Array of strings, each element is an item id.
- `user_id.json`: Array of integers, each element is a user id.
- `user_key.json`: List of user keys (custom content).
- `order_items.json`: Array of objects, each object contains fields such as `order_id`, `amount`.
- `template.jsonnet`: Defines the output structure.