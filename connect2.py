import gtk
class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Hello World in PyGTK")
      self.set_default_size(400,300)
      self.set_position(gtk.WIN_POS_CENTER)
		
      self.label = gtk.Label("Enter name")
      self.entry = gtk.Entry()
      self.btn = gtk.Button("Say Hello")
      self.btn.connect("button_press_event", self.hello)
		
      fixed = gtk.Fixed()
      fixed.put(self.label, 100,100)
      fixed.put(self.entry, 100,125)
      fixed.put(self.btn,100,150)
		
      self.add(fixed)
      self.show_all()
		
   def hello(self,widget,event):
      print "hello",self.entry.get_text()

PyApp()
gtk.main()
