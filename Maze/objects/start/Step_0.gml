/// @DnDAction : YoYo Games.Mouse & Keyboard.If_Key_Pressed
/// @DnDVersion : 1
/// @DnDHash : 03F01B8E
/// @DnDArgument : "key" "vk_anykey"
var l03F01B8E_0;
l03F01B8E_0 = keyboard_check_pressed(vk_anykey);
if (l03F01B8E_0)
{
	/// @DnDAction : YoYo Games.Rooms.Go_To_Room
	/// @DnDVersion : 1
	/// @DnDHash : 421BD335
	/// @DnDParent : 03F01B8E
	/// @DnDArgument : "room" "roommaze"
	/// @DnDSaveInfo : "room" "b6b2eb5c-04c5-43f6-923d-69903ada46ad"
	room_goto(roommaze);
}

/// @DnDAction : YoYo Games.Mouse & Keyboard.If_Mouse_Pressed
/// @DnDVersion : 1.1
/// @DnDHash : 51F22273
/// @DnDArgument : "button" "mb_any"
var l51F22273_0;
l51F22273_0 = mouse_check_button_pressed(mb_any);
if (l51F22273_0)
{
	/// @DnDAction : YoYo Games.Rooms.Go_To_Room
	/// @DnDVersion : 1
	/// @DnDHash : 0C07271F
	/// @DnDParent : 51F22273
	/// @DnDArgument : "room" "roommaze"
	/// @DnDSaveInfo : "room" "b6b2eb5c-04c5-43f6-923d-69903ada46ad"
	room_goto(roommaze);
}