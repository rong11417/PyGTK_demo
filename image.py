import gtk

class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      
      self.set_title("PyGtk Image demo")
      self.set_size_request(800, 600)
      self.set_position(gtk.WIN_POS_CENTER)
      
      image1 = gtk.Image()
      image1.set_from_file("timg.jpg")
      self.add(image1)
      self.connect("destroy", gtk.main_quit)
      self.show_all()

PyApp()
gtk.main()
