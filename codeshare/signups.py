from fltk import * # FLTK :((

class SignupWindow(Fl_Double_Window):
    """App to process signups for the school coding club."""
    
    def __init__(self, label="Eric Hamber Coding Club"):
        super().__init__(*self.determine_position(), label)

        title = Fl_Box(round(self.w()/2-250), 15, 400, 50, "JOIN CODING CLUB!")
        title.labelsize(30)
        title.align(FL_ALIGN_INSIDE | FL_ALIGN_LEFT)

        form_y = round(self.h() * 0.125)
        name_w = round(self.w() / 4)
        number_x = 30 + name_w + 30
        number_w = round(self.w()/12)
        email_x = number_x + number_w + 30
        email_w = round(self.w()/3)
        button_x = email_x + email_w + 30

        self.form_group = Fl_Group(30, 0, button_x - 10, 200)

        self.name_inp = Fl_Input(30, form_y, name_w, 30, "Full Name")
        self.name_inp.align(FL_ALIGN_TOP | FL_ALIGN_LEFT)
        self.number_inp = Fl_Int_Input(number_x, form_y, number_w, 30, "Student Number")
        self.number_inp.align(FL_ALIGN_TOP | FL_ALIGN_LEFT)
        self.email_inp = Fl_Input(email_x, form_y, email_w, 30, "Preferred email")
        self.email_inp.align(FL_ALIGN_TOP | FL_ALIGN_LEFT)

        self.form_group.end()
        self.form_group.resizable(self)

        self.submit_button = Fl_Return_Button(button_x, form_y - 5, 120, 40,"Join Club")

        w = self.w() - 60
        h = round((self.h() * 0.80) - 60)
        x = round((self.w() - w) / 2)
        y = round((self.h() * 0.20) + 30) 
        self.students_browser = Col_Resize_Browser(x, y, w, h, "Coding Club Members:")
        self.students_browser.labelsize(19)
        self.students_browser.align(FL_ALIGN_TOP | FL_ALIGN_LEFT)

        # Use format characters to change text & bg colour + make bold
        self.columnnames = '@B8@C7@b@.NAME\t@B8@C7@b@.STUDENT NUMBER\t@B8@C7@b@.EMAIL'
        
        # Required for Col_Resize_Browser, maybe not pythonic but it's not really my logic
        widths = (250, 200, 100, 0)
        self.students_browser.widths = list(widths[:-1])
        
        # Create columns
        self.students_browser.column_widths(widths)
        self.students_browser.add(self.columnnames)

        self.end()
        self.load_students()
        self.add_students()
        self.resizable(self.students_browser)

    def determine_position(self):
        screen_w = Fl.w()
        screen_h = Fl.h()

        w = round(screen_w * 0.75)
        h = round(screen_h * 0.75)
        x = round((screen_w - w) / 2)
        y = round((screen_h - h) / 2)
        return x, y, w, h

    def load_students(self):
        try:
            with open("members.txt", "r") as f:
                self.students = [l.strip().split(",") for l in f.readlines()]
              
        except FileNotFoundError:
            self.students = []

    def add_students(self):
        for student in self.students:
            if self.students_browser.size() % 2 == 0:
                line = "@B23" + "\t@B23 ".join(student)
            else:
                line = "\t ".join(student)
            self.students_browser.add(line)

    def save_students(self):
        with open('members.txt', 'w') as f:
            f.write("\n".join([",".join(student) for student in self.students]))


class Col_Resize_Browser(Fl_Hold_Browser):
    """Fl_Hold_Browser with resizing columns.
    
    Logic and most of implementation translated into python from:
        http://seriss.com/people/erco/fltk/#Fl_Resize_Browser

    Differences include Fl_Hold_Browser selecting behavior and top-bottom
    wrapping with arrow keys.

    """

    def __init__(self, x, y, w, h, label=None):
        """Initialize an instance.
        
        All class-specific attributes are not arguments, which I'm
        not sure how I feel about. I guess it prevents super long lines
        when creating instances.
        """

        super().__init__(x, y, w, h, label)
        
        self.colsepcolor = FL_BLACK
        self.showcolsep = True
        self.last_curs = FL_CURSOR_DEFAULT
        self.drag_col = -1
        self.widths = list()
        self.nowidths = list()

        # For wrapping with arrow keys
        self._lastvalue = 0

    def change_cursor(self, newcursor):
        """Change cursor if not already set to specified value."""

        if newcursor == self.last_curs:
            return
        
        self.window().cursor(newcursor)
        
        self.last_curs = newcursor
    
    def bbox(self):
        """Get the inside dimensions of browser not including scorll bars.
        
        Assumes a width of 1 px for the box.
        """

        vert_visible = self.getScrollbar().visible()
        hori_visible = self.getHScrollbar().visible()

        if vert_visible or hori_visible:
            sb_size = Fl.scrollbar_size()

        x = self.x() + 1
        y = self.y() + 1

        w = self.w() - 2 - sb_size if vert_visible else self.w() - 2
        h = self.h() - 2 - sb_size if hori_visible else self.h() - 2

        return x, y, w, h

    def col_near_mouse(self):
        """Return the column the mouse is near or -1 if none."""
        
        x, y, w, h = self.bbox()
        
        # Not inside browser area (eg. on a scrollbar)
        if not Fl.event_inside(x, y, w, h):
            return -1
        
        mousex = Fl.event_x() + self.hposition()
        colx = self.x()
        
        for t in range(len(self.widths) - 1):
            colx += self.widths[t]
            
            diff = mousex - colx
            
            # Return column number if mouse nearby
            if -4 <= diff <= 4:
                return t
        
        return -1
    
    def recalc_hscroll(self):
        """Sync horizontal scrollbar as columns are dragged."""

        vertpos = self.position()
        select = self.value()

        # Changing textsize() triggers recalc of scrollbars
        size = self.textsize()
        self.textsize(size + 1)
        self.textsize(size)

        # It also resets some other stuff so need to set these again
        self.position(vertpos)
        self.value(select)
    
    def handle(self, event):
        """Extend Fl_Browser.handle to manage events for column resizing."""

        # Not entirely sure what the point of this is, if you wanted 
        # this you could just not use this class, but it's in the 
        # original Col_Resize_Browser
        if not self.showcolsep:
            return super().handle(event)
        
        if event == FL_MOVE:
            if self.col_near_mouse() == -1:
                self.change_cursor(FL_CURSOR_DEFAULT)
            else:
                self.change_cursor(FL_CURSOR_WE)
        
        elif event == FL_PUSH:
            col = self.col_near_mouse()
            
            # Start dragging if clicked on resizer
            if col >= 0: 
                self.drag_col = col
                return 1 # Eclipse Fl_Browser handle, don't select item
            
            super().handle(event)
            
            # If clicked on column titles, deselect
            if self.value() == 1:
                self.select(1, 0)
            
            self.do_callback()
            return 1
        
        elif event == FL_DRAG:
            if self.drag_col != -1:
                # Sum up column widths to determine position
                mousex = Fl.event_x() + self.hposition()
                newwidth = mousex - self.x()
                
                for t in range(len(self.widths) - 1):
                    if t >= self.drag_col:
                        break
                    
                    newwidth -= self.widths[t]
                
                if newwidth > 0:
                    self.widths[self.drag_col] = newwidth
                    # Apply new widths and redraw
                    self.column_widths(tuple(self.widths + [0]))
                    self.recalc_hscroll()
                    self.redraw()

                return 1
            
            super().handle(event)

            # If drag selecting onto column titles, deselect
            if self.value() == 1:
                self.select(1, 0)
            return 1

        
        elif event == FL_RELEASE:
            # Exit drag mode
            self.drag_col = -1
            self.change_cursor(FL_CURSOR_DEFAULT)
            return 1

            """Strange thing in original code here:
            if ( e == FL_RELEASE ) return 1;        // eclipse event
                ret = 1;
                break;
            
            But my code seems to be working fine.
            """

        elif event == FL_KEYDOWN:
            if Fl.event_key() == FL_Up and self._lastvalue == 2:
                self.value(self.size())
                self.bottomline(self.value())
                self.do_callback()
                return 1

            elif Fl.event_key() == FL_Down and self._lastvalue == self.size():
                self.value(2)
                self.do_callback()
                return 1
        
        self._lastvalue = self.value()
        
        return super().handle(event)
    
    def draw(self):
        """Extend Fl_Browser.draw to draw column separators."""

        super().draw()
        
        if self.showcolsep:
            # Draw column separators

            colx = self.x() - self.hposition()
            
            # Don't draw over scrollbars
            x, y, w, h = self.bbox()
            
            fl_color(self.colsepcolor)
            
            for t in range(len(self.widths) - 1):
                colx += self.widths[t]
                
                # Only draw if within browser
                if x < colx < (x + w):
                    fl_line(colx, y, colx, y+h-1)

if __name__ == "__main__":
    window = SignupWindow()
    window.show()
    Fl.run()