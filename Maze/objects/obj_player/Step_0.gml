/// @DnDAction : YoYo Games.Collisions.If_Object_At
/// @DnDVersion : 1
/// @DnDHash : 48C9C939
/// @DnDArgument : "x" "obj_player.x"
/// @DnDArgument : "y" "obj_player.y"
/// @DnDArgument : "object" "obj_wall"
/// @DnDSaveInfo : "object" "6e78658d-2068-4fdc-8b62-f84c28f975b4"
var l48C9C939_0 = instance_place(obj_player.x, obj_player.y, obj_wall);
if ((l48C9C939_0 > 0))
{
	/// @DnDAction : YoYo Games.Rooms.Go_To_Room
	/// @DnDVersion : 1
	/// @DnDHash : 53367025
	/// @DnDParent : 48C9C939
	/// @DnDArgument : "room" "roombad"
	/// @DnDSaveInfo : "room" "fc3c1a2f-7323-44cf-95f3-6f5a2c6d4a89"
	room_goto(roombad);
}

/// @DnDAction : YoYo Games.Common.If_Variable
/// @DnDVersion : 1
/// @DnDHash : 68D6CD78
/// @DnDArgument : "var" "points"
/// @DnDArgument : "op" "4"
/// @DnDArgument : "value" "30"
if(points >= 30)
{
	/// @DnDAction : YoYo Games.Rooms.Go_To_Room
	/// @DnDVersion : 1
	/// @DnDHash : 5F6B2909
	/// @DnDParent : 68D6CD78
	/// @DnDArgument : "room" "roomgood"
	/// @DnDSaveInfo : "room" "e7a1e985-67c8-4348-9685-9ae23717340e"
	room_goto(roomgood);
}

/// @DnDAction : YoYo Games.Collisions.If_Object_At
/// @DnDVersion : 1
/// @DnDHash : 3F1FDDDD
/// @DnDArgument : "x" "obj_player.x"
/// @DnDArgument : "y" "obj_player.y"
/// @DnDArgument : "object" "obj_prize"
/// @DnDSaveInfo : "object" "3512a578-537e-4422-926b-dd0a08a47810"
var l3F1FDDDD_0 = instance_place(obj_player.x, obj_player.y, obj_prize);
if ((l3F1FDDDD_0 > 0))
{
	/// @DnDAction : YoYo Games.Common.Variable
	/// @DnDVersion : 1
	/// @DnDHash : 3B7FE26F
	/// @DnDParent : 3F1FDDDD
	/// @DnDArgument : "expr" "1"
	/// @DnDArgument : "expr_relative" "1"
	/// @DnDArgument : "var" "points"
	points += 1;
}