type typeProgram = __Program

type typeEventManager = __EventManager
type typeProcessManager = __ProcessManager
type typeFramerateManager = __FramerateManager
type typeDrawManager = __DrawManager
type typeWindowManager = __WindowManager

type typeProcessableObject = __ProcessableObject
type typeGraphicObject = __GraphicObject
type typeContainer = __Container

type typePygameWindow = __PygameWindow


from pygame import Window as __PygameWindow

from .managers import DrawManager as __DrawManager
from .managers import EventManager as __EventManager
from .managers import FramerateManager as __FramerateManager
from .managers import ProcessManager as __ProcessManager
from .managers import WindowManager as __WindowManager
from .objects import Container as __Container
from .objects import GraphicObject as __GraphicObject
from .objects import ProcessableObject as __ProcessableObject
from .program import Program as __Program
