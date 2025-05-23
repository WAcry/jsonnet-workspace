local user_key = std.parseJson(std.extVar('user_key'));
local user_id = std.parseJson(std.extVar('user_id'));
local item_ids = std.parseJson(std.extVar('item_ids'));
local order_items = std.parseJson(std.extVar('order_items'));

{
  user_key: user_key,
  user_id: user_id,
  item_ids: item_ids,
  order_items: order_items,
}

