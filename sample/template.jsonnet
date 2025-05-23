local user_key = std.parseJson(std.extVar('user_key'));
local user_id = std.parseJson(std.extVar('user_id'));
local item_ids = std.parseJson(std.extVar('item_ids'));

{
  user_key: user_key,
  user_id: user_id,
  item_ids: item_ids,
}