set OUTPUTDIR=output
set PELICANCONF=pelicanconf.py

call make_venv.bat
call env\Scripts\activate.bat

pip install -r requirements.txt

pelican content -o %OUTPUTDIR% -s %PELICANCONF%

cd %OUTPUTDIR%
pelican -l
