import gtk

class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("EventBox demo")
      self.set_size_request(200,100)
      self.set_position(gtk.WIN_POS_CENTER)
      fixed = gtk.Fixed()
      
      event1 = gtk.EventBox()
      label1 = gtk.Label("Label 1")
      event1.add(label1)
      fixed.put(event1, 80,20)
      
      event1.connect("button_press_event",self.hello1)
      event2 = gtk.EventBox()
      label2 = gtk.Label("Label 2")
      event2.add(label2)
      event2.connect("button_press_event",self.hello2)
      fixed.put(event2, 80,70)
      
      self.add(fixed)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
		
   def hello1(self, widget, event):
      print "clicked label 1"
		
   def hello2(self, widget, event):
      print "clicked label 2"

PyApp()
gtk.main()
