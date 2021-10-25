The programme are in two parts

###1. 
split item.py
- split item by category

###2.
Three main files for the programme 
1. main.py
2. hktvmall_keyword_classify.py
3. run.py

the output file folders
- classify folder - /classification for hktvmall item files in .csv 
- make db folder - / database files in .db
- item result fodler - / result file in .xlsx 

To run the programme 
1. edit hktvmall_keyword_classify.py
2. run run.py
    - enter the variables for run the programme, result(category1,category2, function, filename, code1, code2, number)
    - category1 ------ the first category of item belongs to
    - category2 ------ the second category of item belongs to
    - function ------ classification function name, found in hktvmall_keyword_classify.py
    - filename ------ the output filename wanted
    - code1 ------ the first CPICode for the category
    - code2 ------ the second CPICode for the category
    - number ------ number order, acs by order of CPICode


