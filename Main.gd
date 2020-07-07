extends Control

onready var LABEL_STATUS: Label = self.find_node("LabelStatus", true, false)


onready var BUTTON_RUN_DEMO: Button = self.find_node("ButtonRunDemo", true, false)


onready var LABEL_RESULT_JOIN: Label = self.find_node("LabelResultJoin", true, false)
onready var LABEL_RESULT_ADD: Label = self.find_node("LabelResultAdd", true, false)
onready var LABEL_RESULT_MSG: Label = self.find_node("LabelResultMessage", true, false)

onready var INPUT_STRING_1: LineEdit = self.find_node("InputString1", true, false)
onready var INPUT_STRING_2: LineEdit = self.find_node("InputString2", true, false)

onready var INPUT_NUMBER_1: Range = self.find_node("InputNumber1", true, false)
onready var INPUT_NUMBER_2: Range = self.find_node("InputNumber2", true, false)

onready var INPUT_MSG_OFFSET: Range = self.find_node("InputMsgOffset", true, false)
onready var INPUT_MSG_LENGTH: Range = self.find_node("InputMsgLength", true, false)


var _foreigner = null
var _testlib = null


func _ready() -> void:

    self._foreigner = load('res://addons/testlib/testlib.gdns').new()

    if self._foreigner:
        LABEL_STATUS.text = "Loaded."

        BUTTON_RUN_DEMO.grab_focus()

    else:
        LABEL_STATUS.text = "Not loaded."

        BUTTON_RUN_DEMO.disabled = true


    randomize()
    INPUT_NUMBER_1.value = randi() % 99
    INPUT_NUMBER_2.value = randi() % 99


func run_demo():

    if not self._testlib:

        var library_path: String = SharedLibrary.testlib[OS.get_name()]
        library_path = SharedLibrary.testlib._Base_.plus_file(library_path)

        self._testlib = _foreigner.open(Utils._get_correct_path(library_path))

        if not self._testlib:
            return

        self._testlib.define('add2i', 'sint32', ['sint32', 'sint32'])
        self._testlib.define('joinStrings', 'string', ['string', 'string'])
        self._testlib.define('getMessage', 'pointer', []) # Actually 'string' but we want to do pointer manipulation.


    LABEL_RESULT_ADD.text = "%d" % self._testlib.invoke('add2i', [int(INPUT_NUMBER_1.value), int(INPUT_NUMBER_2.value)])

    LABEL_RESULT_JOIN.text = self._testlib.invoke('joinStrings', [INPUT_STRING_1.text, INPUT_STRING_2.text])

    var msg_ptr = self._testlib.invoke('getMessage', [])

    if msg_ptr != 0:
        var _op = _foreigner.new_buffer(8) # Workaround for lack of static class methods.
        LABEL_RESULT_MSG.text = _op.string_at(_op.offset(msg_ptr, int(INPUT_MSG_OFFSET.value)), int(INPUT_MSG_LENGTH.value))
    else:
        LABEL_RESULT_MSG.text = "Pointer was: 0x%08x" % msg_ptr


func _on_ButtonRunDemo_pressed() -> void:
    self.run_demo()
