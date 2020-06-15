extends Control

onready var LABEL_STATUS: Label = self.find_node("LabelStatus", true, false)

var foreigner = preload('res://addons/foreigner/foreigner.gdns').new()


func _ready() -> void:

    if self.foreigner:
        LABEL_STATUS.text = "Loaded."
    else:
        LABEL_STATUS.text = "Not loaded."
