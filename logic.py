# import pandas lib as pd
import os   
import xlrd
FILE_PATH=''
def gen_date(date):
    day = date.split('/')[0]
    month = date.split('/')[1]
    year = str(date.split('/')[2])[2:4]
    # if int(day) < 10:
    #     day = f'0{day}'
    # if int(month) < 10:
    #     month = f'0{month}'    
    pricestring = f"j000000{day}{month}{year}00000000000000000000"
    return pricestring
def generate_str(sh_obj=None,n_rows=0,n_cols=0):    
    pricestring="\nj"
    for cy in range(1,n_cols):
        end_str=0
        for rx in range(2,n_rows):
            SNF=f"0{round(sh_obj.cell_value(1,cy)*10)}"
            if(len(SNF)>3):
                SNF=f"{round(sh_obj.cell_value(1,cy)*10)}"
            FAT=f"0{round(sh_obj.cell_value(rx,0)*10)}"
            if(len(FAT)>3):
                FAT=f"{round(sh_obj.cell_value(rx,0)*10)}"
            RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2)*100)                 
            if len(str(RATE))==5 :
                RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2)*10)                 
            elif len(str(RATE))>5 :
                RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2))                 
            # gen string
            if(end_str>=3 and rx!=n_rows-1):                
                pricestring+='00\n'
                pricestring+=f"j{SNF}{FAT}{RATE}"
                end_str=1
            elif(rx==n_rows-1):                
                if end_str==1:
                    pricestring+='0000000000000000000000'
                elif end_str==2:
                    pricestring+='000000000000'
                else:
                    pricestring+='00'
                end_str=0
                # remove j from the end of the file
                if(not (cy == n_cols-1 and rx == n_rows-1)):                    
                    pricestring+='\nj'                
            else:
                pricestring+=f"{SNF}{FAT}{RATE}"
                end_str+=1              
    return pricestring

def gen_data(file_path):
    FILE_PATH=file_path
    if(os.path.exists(FILE_PATH)):
        book=xlrd.open_workbook(FILE_PATH)        
        # Effectivate date
        sh = book.sheet_by_index(4)
        date=sh.cell_value(1,0)
        data1=gen_date(date)
        # Cow
        # sh = book.sheet_by_index(0)
        # n_rows=sh.nrows
        # n_cols=sh.ncols
        # data2=generate_str(sh_obj=sh,n_rows=n_rows,n_cols=n_cols)
        # Buffalo
        sh = book.sheet_by_index(1)
        n_rows=sh.nrows
        n_cols=sh.ncols
        data3=generate_str(sh_obj=sh,n_rows=n_rows,n_cols=n_cols)                
        data=data1+data3        
        return 1,data
    else:
        return 0,"Error"