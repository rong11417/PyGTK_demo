import gtk

class PyApp(gtk.Window):
   
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Range widgets Demo")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      adj1 = gtk.Adjustment(0.0, 0.0, 101.0, 0.1, 1.0, 1.0)
      self.adj2 = gtk.Adjustment(10,0,101,5,1,1)
      
      scale1 = gtk.HScale(adj1)
      scale1.set_update_policy(gtk.UPDATE_CONTINUOUS)
      scale1.set_digits(1)
      scale1.set_value_pos(gtk.POS_TOP)
      scale1.set_draw_value(True)
      
      vb = gtk.VBox()
      vb.add(scale1)
      lbl1 = gtk.Label("HScale")
      
      vb.add(lbl1)
      self.bar1 = gtk.HScrollbar(self.adj2)
      self.bar1.set_update_policy(gtk.UPDATE_CONTINUOUS)
      vb.add(self.bar1)
      self.lbl2 = gtk.Label("HScrollbar value: ")
      
      vb.add(self.lbl2)
      self.adj2.connect("value_changed", self.on_scrolled)
      self.add(vb)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
   
   def on_scrolled(self, widget, data=None):
      self.lbl2.set_text("HScrollbar value: "+str(int(self.adj2.value)))
if __name__ == '__main__':
   PyApp()
   gtk.main()
