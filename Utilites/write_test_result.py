from Utilites import XLUtils

# path = r"D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx\E-Commerce-data.xlsx"
# rows = XLUtils.getRowCout(path, 'Sheet1')


def write_result(flag,r):
    path = "D:\Product-Compare-Muti-Sites\Results\E-Commerce-data.xlsx"
    # rows = XLUtils.getRowCout(path, 'Sheet1')
    if flag:
        # print("Test Passed...")
        XLUtils.writeData(path, 'Sheet1', r, 2, 'Pass')

    else:
        # print("Failed...")
        XLUtils.writeData(path, 'Sheet1', r, 2, 'Fail')

def write_product_result(company_name,value,r):
    path = r"D:\GitHub\Compare-Ecommerce-Website\Results\finaldata.xlsx"
    XLUtils.writeData(path, 'Sheet1', r, 2, company_name)
    XLUtils.writeData(path, 'Sheet1', r, 3, value)
