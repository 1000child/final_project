/// @DnDAction : YoYo Games.Mouse & Keyboard.If_Mouse_Pressed
/// @DnDVersion : 1.1
/// @DnDHash : 5C93AB8B
/// @DnDArgument : "button" "mb_any"
var l5C93AB8B_0;
l5C93AB8B_0 = mouse_check_button_pressed(mb_any);
if (l5C93AB8B_0)
{
	/// @DnDAction : YoYo Games.Game.End_Game
	/// @DnDVersion : 1
	/// @DnDHash : 48E2D5A6
	/// @DnDParent : 5C93AB8B
	game_end();
}

/// @DnDAction : YoYo Games.Mouse & Keyboard.If_Key_Pressed
/// @DnDVersion : 1
/// @DnDHash : 248E938B
/// @DnDArgument : "key" "vk_anykey"
var l248E938B_0;
l248E938B_0 = keyboard_check_pressed(vk_anykey);
if (l248E938B_0)
{
	/// @DnDAction : YoYo Games.Game.End_Game
	/// @DnDVersion : 1
	/// @DnDHash : 4B57B344
	/// @DnDParent : 248E938B
	game_end();
}