import pandas

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300,300,50],
    "Price": [1,.5,.75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Packaging"],
    "Price":[25,35,10]
}

variable_cost_frame = pandas.DataFrame(variable_dict)
fixed_cost_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"

profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

heading = "****{}****".format(product_name)
profit_target_sentence = "Profit Target: {}".format(profit_target)
required_sales_sentence = "Required Sales: {}".format(required_sales)
recommended_price_sentence = "Recommended Sales: {}".format(recommended_price)

# Chnage data frame to string so it can be written to txt file
variable_cost_txt = pandas.DataFrame.to_string(variable_cost_frame)
fixed_cost_txt = pandas.DataFrame.to_string(fixed_cost_frame)

#list holding stuff to print/write to file
to_write = [heading,variable_cost_txt,fixed_cost_txt,profit_target_sentence,required_sales_sentence,recommended_price_sentence]


# Wirte to file
#create file to hold data add .txt extension 
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# write items to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close Text File
text_file.close()

# print the stuff
for item in to_write:
    print(item)
    print()