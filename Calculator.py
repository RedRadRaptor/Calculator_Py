import Tkinter as tk
from tkFont import Font
import numpy as np

def call_Graph():
    win1 = tk.Toplevel(root)
    win1.title("Graph")
    return

def widget(w_type, root, tex, x_cord, y_cord, f_size, w_height, w_width):
    
    if w_type is "button":
        w_out = tk.Button(root, text = tex, height = w_height, width= w_width)
        f_name = Font(size = f_size)
        w_out['font'] = f_name
    elif w_type is "label":
        w_out = tk.Label(root, text = tex, height = w_height, width= w_width)
        f_name = Font(size = f_size)
        w_out['font'] = f_name
    elif w_type is "entry":
        w_out = tk.Entry(height = w_height, width= w_width)
    w_out.place(x = x_cord, y = y_cord)
    return [w_out]

if __name__ == "__main__":
    #Setting up main window
    root = tk.Tk()
    root.title('Calculator')
    root.minsize(400, 400)
    
    #Output frame set up
    frm_output = tk.Frame(root, width=300, height=50, bg = "white", highlightbackground = "black", highlightthickness = 1)
    frm_output.pack()
    frm_output.pack_propagate(False)
    
    #Standard text and widget size
    f_size = 20
    w_height = 1
    w_width = 2
    
    #Setting up output window label variable to later manipulate
    out_label = tk.Label(frm_output,text='',bg='white')
    out_label.pack(side=tk.LEFT)
    
    def print_val(out,btn):
        #input from user
        in_text = btn[0].cget('text')
        
        #previous output in window
        out_text = out.cget('text')
        
        #adding character to window
        if (out_text == '') or (out_text == 'ENT_ERROR'):
            out.config(text=in_text,font=('Helvetica bold', 25))
        else:
            in_text = out_text+in_text
            out.config(text=in_text,font=('Helvetica bold', 25))
    def delete(out):
        #previous output in window
        out_text = out.cget('text')
        
        #Changing text to exclude last cha
        out_text = out_text[0:len(out_text)-1]
        out.config(text=out_text,font=('Helvetica bold', 25))
    def clear(out):
        out_text = out.cget('text')
        out_text = ''
        out.config(text=out_text,font=('Helvetica bold', 25))
    def append_obj(list, obj_list):
        for item in obj_list:
                list.append(item)
    def opp_iteration(out_items,opp_vec):
        
        #Setting up empty arrays
        mult_ind =[]
        div_ind=[]
        add_ind=[]
        min_ind=[]
        
        #Index for, FOR loop
        index_opp_vec = 0
        
        ##PEMDAS algorithm
        for opp in opp_vec:
            opp_ind = out_items.index(opp, index_opp_vec)
            if opp is '*':
                mult_ind.append(opp_ind)
            elif opp is '/':
                div_ind.append(opp_ind)
            elif opp is '+':
                add_ind.append(opp_ind)
            elif opp is '-':
                min_ind.append(opp_ind)
            index_opp_vec = opp_ind+1
        
        ##Appending opperator indices into a single array in order of PEMDAS
        opp_ind = []
        if mult_ind != []:
            append_obj(opp_ind, mult_ind)
        if div_ind != []:
            append_obj(opp_ind, div_ind)
        if add_ind != []:
            append_obj(opp_ind, add_ind)
        if min_ind != []:
            append_obj(opp_ind, min_ind)
        return opp_ind
    def enter(out):
        #previous output in window
        out_text = out.cget('text')
        out_objects = []
        opp_vec = []
        st_ind = 0
        end_ind = 0
        
        #Dividing objects in screen into its separate elements
        for cha in out_text:
            if (cha is '+') or (cha is '-') or (cha is '*') or (cha is '/'):
                out_objects.append(out_text[st_ind:end_ind])
                out_objects.append(cha)
                opp_vec.append(cha)
                st_ind = end_ind + 1
            end_ind = end_ind + 1
        out_objects.append(out_text[st_ind:end_ind])
        opp_ind = opp_iteration(out_objects,opp_vec)
        
        #Performing operations on digits in window
        opp_ind_vec = opp_ind
        for x in range(len(opp_vec)):
            ind = opp_ind_vec[0]
            end_st = len(out_objects)
            
            #Using operators to perform action to digits next to it
            op = out_objects[ind]
            if op is '*':
                num_1 = float(out_objects[ind-1])
                num_2 = float(out_objects[ind+1])
                num_3 = num_1 * num_2
            elif op is '/':
                num_1 = float(out_objects[ind-1])
                num_2 = float(out_objects[ind+1])
                num_3 = num_1 / num_2
            elif op is '+':
                num_1 = float(out_objects[ind-1])
                num_2 = float(out_objects[ind+1])
                num_3 = num_1 + num_2
            elif op is '-':
                num_1 = float(out_objects[ind-1])
                num_2 = float(out_objects[ind+1])
                num_3 = num_1 - num_2
            
            #Stacking the operated digit back into the objects array
            out_objects_1 = out_objects[0:ind-1]
            out_objects_3 = out_objects[ind+2:end_st]
            out_objects_1.append(str(num_3))
            append_obj(out_objects_1, out_objects_3)
            out_objects = out_objects_1
            
            #STOP condition for the FOR Loop
            if len(out_objects) == 1:
                break
            
            #Shrinking operations left in output window
            opp_vec.pop(((ind+1)/2)-1)
            opp_ind_vec = opp_iteration(out_objects,opp_vec)
        
        #Printing the resulting digit
        out_print = str(out_objects[0])
        out.config(text=out_print,font=('Helvetica bold', 25))
        return
    
    #Digit Buttons
    btn_7 = widget("button",root,"7",50,110,f_size,w_height,w_width)
    btn_7[0].configure(command=lambda: print_val(out_label,btn_7))
    
    btn_8 = widget("button",root,"8",90,110,f_size,w_height,w_width)
    btn_8[0].configure(command=lambda: print_val(out_label,btn_8))
    
    btn_9 = widget("button",root,"9",130,110,f_size,w_height,w_width)
    btn_9[0].configure(command=lambda: print_val(out_label,btn_9))
    
    btn_4 = widget("button",root,"4",50,170,f_size,w_height,w_width)
    btn_4[0].configure(command=lambda: print_val(out_label,btn_4))
    
    btn_5 = widget("button",root,"5",90,170,f_size,w_height,w_width)
    btn_5[0].configure(command=lambda: print_val(out_label,btn_5))
    
    btn_6 = widget("button",root,"6",130,170,f_size,w_height,w_width)
    btn_6[0].configure(command=lambda: print_val(out_label,btn_6))
    
    btn_1 = widget("button",root,"1",50,230,f_size,w_height,w_width)
    btn_1[0].configure(command=lambda: print_val(out_label,btn_1))
    
    btn_2 = widget("button",root,"2",90,230,f_size,w_height,w_width)
    btn_2[0].configure(command=lambda: print_val(out_label,btn_2))
    
    btn_3 = widget("button",root,"3",130,230,f_size,w_height,w_width)
    btn_3[0].configure(command=lambda: print_val(out_label,btn_3))
    
    #btn_neg = widget("button",root,"(-)",50,290,f_size,w_height,w_width)
    #btn_neg[0].configure(command=lambda: print_val(btn_neg))
    
    btn_0 = widget("button",root,"0",90,290,f_size,w_height,w_width)
    btn_0[0].configure(command=lambda: print_val(out_label,btn_0))
    
    btn_deci = widget("button",root,".",130,290,f_size,w_height,w_width)
    btn_deci[0].configure(command=lambda: print_val(out_label,btn_deci))
    
    #Operator Buttons
    btn_del = widget("button",root,"delete",220,110,10,3,4)
    btn_del[0].configure(command=lambda: delete(out_label))
    
    btn_clr = widget("button",root,"clear",220,170,10,3,4)
    btn_clr[0].configure(command=lambda: clear(out_label))
    
    btn_ent = widget("button",root,"=",220,230,f_size,w_height,w_width)
    btn_ent[0].configure(command=lambda: enter(out_label))
    
    btn_min = widget("button",root,"-",170,110,f_size,w_height,w_width)
    btn_min[0].configure(command=lambda: print_val(out_label,btn_min))
    
    btn_plus = widget("button",root,"+",170,170,f_size,w_height,w_width)
    btn_plus[0].configure(command=lambda: print_val(out_label,btn_plus))
    
    btn_div = widget("button",root,"/",170,230,f_size,w_height,w_width)
    btn_div[0].configure(command=lambda: print_val(out_label,btn_div))
    
    btn_mult = widget("button",root,"*",170,290,f_size,w_height,w_width)
    btn_mult[0].configure(command=lambda: print_val(out_label,btn_mult))
    
    btn_Graph = tk.Button(root, text="Graph Function", command=call_Graph)
    btn_Graph.pack()
    
    root.mainloop()