extends Control

onready var LABEL_STATUS: Label = self.find_node("LabelStatus", true, false)

var _foreigner = preload('res://addons/foreigner/foreigner.gdns').new()

onready var BUTTON_RUN_DEMO: Button = self.find_node("ButtonRunDemo", true, false)


onready var LABEL_RESULT_JOIN: Label = self.find_node("LabelResultJoin", true, false)
onready var LABEL_RESULT_ADD: Label = self.find_node("LabelResultAdd", true, false)

onready var INPUT_STRING_1: LineEdit = self.find_node("InputString1", true, false)
onready var INPUT_STRING_2: LineEdit = self.find_node("InputString2", true, false)

onready var INPUT_NUMBER_1: Range = self.find_node("InputNumber1", true, false)
onready var INPUT_NUMBER_2: Range = self.find_node("InputNumber2", true, false)




func _ready() -> void:

    if self._foreigner:
        LABEL_STATUS.text = "Loaded."
    else:
        LABEL_STATUS.text = "Not loaded."
