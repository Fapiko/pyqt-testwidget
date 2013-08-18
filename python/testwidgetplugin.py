from PyQt4.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt4.QtGui import QIcon
from testwidget import TestWidget


class TestWidgetPlugin(QPyDesignerCustomWidgetPlugin):
	def __init__(self, parent=None):
		QPyDesignerCustomWidgetPlugin.__init__(self)

	def name(self):
		return 'TestWidget'

	def group(self):
		return 'Fapiko.Com Example Widgets'

	def icon(self):
		return QIcon()

	def isContainer(self):
		return False

	def includeFile(self):
		return 'testwidget'

	def toolTip(self):
		return 'Arnold Facepalmer'

	def whatsThis(self):
		return 'Facepalm all day'

	def createWidget(self, parent):
		return TestWidget(parent)
