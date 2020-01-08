import gtk

class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_default_size(300,200)
      self.set_title("Hello World in PyGTK")
      
      fixed=gtk.Fixed()
      btn=gtk.Button("Hello World")
      fixed.put(btn,100,100)
      self.add(fixed)
      self.show_all()
PyApp()
gtk.main() #run event loop
