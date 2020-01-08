import gtk

class PyApp(gtk.Window):
  def __init__(self):
    super(PyApp,self).__init__()
    
    self.set_title("Button box demo")
    self.set_size_request(200,100)
    self.set_position(gtk.WIN_POS_CENTER)
    
    vb=gtk.VBox()
    box1=gtk.VButtonBox()
    btn1=gtk.Button(stock=gtk.STOCK_OK)
    btn2=gtk.Button(stock=gtk.STOCK_CANCEL)
  
    box1.pack_start(btn1,True,True,0)
    box1.pack_start(btn2,True,True,0)
    box1.set_border_width(5)

    vb.add(box1)
    
    box2=gtk.HButtonBox()
    btn3=gtk.Button(stock=gtk.STOCK_OK)
    btn4=gtk.Button(stock=gtk.STOCK_CANCEL)
   
    ent=gtk.Entry()
    box2.pack_start(btn3,True,True,0)
    box2.pack_start(btn4,True,True,0)
    box1.set_border_width(5)
    
    vb.add(box2)
    self.add(vb)
    

    self.show_all()


PyApp()
gtk.main()
