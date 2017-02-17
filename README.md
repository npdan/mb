# mb
Sample project.

Buitl using python 2.7 and Django 1.10.
Has a python dependency data-importer (pip install data-importer)

1. Import an XML file into a sqlite database using the command line, preserving updated data and avoiding duplicate SKUs.
   There is a management command.
   From mb/mb directory run:   
      python manage.py xml_item_import -f ../data/import_1.xml
   
2. Create a simple front end UI with the ability to search/filter on the following elements name and sku, not sure what description is, found in the above xml files:
   python manage.py runserver
   http://localhost:8000/products/items/
    
3. Create a simple web form allowing additions, and edits to the data in sqlite. Assume all fields are required. Data validation should be done on the client side. Do not use the Django admin for this. Note: there is no need to worry about preserving imported vs edited data.
    Click on an item in the item list above.
        or
   http://localhost:8000/products/item/462608     
