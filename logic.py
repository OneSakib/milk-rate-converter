# import pandas lib as pd
import os   
import xlrd
import datetime
FILE_PATH=''
dateis = datetime.datetime.now()

def generate_str(sh_obj,n_rows,n_cols):
    day = dateis.day
    month = dateis.month
    year = str(dateis.year)[2:4]
    if day < 10:
        day = f'0{day}'
    if month < 10:
        month = f'0{month}'
    pricestring = f"j000000{day}{month}{year}00000000000000000000\nj"
    for rx in range(2,n_rows):
        end_str=0
        for cy in range(1,n_cols):
            FAT=f"0{round(sh_obj.cell_value(1,cy)*10)}"
            if(len(FAT)>3):
                FAT=f"{round(sh_obj.cell_value(1,cy)*10)}"
            SNF=f"0{round(sh_obj.cell_value(rx,0)*10)}"
            if(len(SNF)>3):
                SNF=f"{round(sh_obj.cell_value(rx,0)*10)}"
            RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2)*100)                 
            if len(str(RATE))==5 :
                RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2)*10)                 
            elif len(str(RATE))>5 :
                RATE=round(round(sh_obj.cell_value(rowx=rx,colx=cy),2))                             
            if(end_str>=3):
                pricestring+='00\n'
                pricestring+=f"j{SNF}{FAT}{RATE}"
                end_str=1
            if(cy==n_cols-1):
                if end_str==1:
                    pricestring+='0000000000000000000000'
                elif end_str==2:
                    pricestring+='000000000000'
                else:
                    pricestring+='00'
                end_str=0
                if(rx != n_rows-1):
                    pricestring+='\nj'
            else:
                pricestring+=f"{SNF}{FAT}{RATE}"
                end_str+=1  
    return pricestring

def gen_data(file_path,sheet_name):
    FILE_PATH=file_path
    if(os.path.exists(FILE_PATH)):
        book=xlrd.open_workbook(FILE_PATH)
        book_sheets_names=book.sheet_names()
        sh = book.sheet_by_name(sheet_name=sheet_name)
        n_rows=sh.nrows
        n_cols=sh.ncols
        data=generate_str(sh_obj=sh,n_rows=n_rows,n_cols=n_cols)
        return 1,data
    else:
        return 0,"Error"