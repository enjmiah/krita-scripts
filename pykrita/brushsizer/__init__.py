from krita import Extension, Krita


SIZES = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    15, 20, 25, 30, 35, 40, 45, 50,
    60, 70, 80, 90, 100,
    125, 150, 175, 200,
    250, 300,
    # Past this point, step by FURTHER_STEP each time.
]
FURTHER_STEP = 100


class BrushSizer(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            "increaseBrushSizeSmart", "Increase Brush Size (Smart)",
            "tools/scripts")
        action.triggered.connect(self.increaseBrushSize)

        action = window.createAction(
            "decreaseBrushSizeSmart", "Decrease Brush Size (Smart)",
            "tools/scripts")
        action.triggered.connect(self.decreaseBrushSize)

    def increaseBrushSize(self):
        window = Application.activeWindow()
        if window and window.views():
            view = window.views()[0]
            currentBrushSize = round(view.brushSize())
            if currentBrushSize >= SIZES[-1]:
                view.setBrushSize(currentBrushSize + FURTHER_STEP)
            else:
                for newSize in SIZES:
                    if newSize > currentBrushSize:
                        view.setBrushSize(newSize)
                        break

    def decreaseBrushSize(self):
        window = Application.activeWindow()
        if window and window.views():
            view = window.views()[0]
            currentBrushSize = round(view.brushSize())
            if currentBrushSize > SIZES[0]:
                if currentBrushSize > SIZES[-1] + FURTHER_STEP:
                    view.setBrushSize(currentBrushSize - FURTHER_STEP)
                else:
                    for newSize in reversed(SIZES):
                        if newSize < currentBrushSize:
                            view.setBrushSize(newSize)
                            break


# Add the extension to Krita's list of extensions.
Krita.instance().addExtension(BrushSizer(Krita.instance()))
