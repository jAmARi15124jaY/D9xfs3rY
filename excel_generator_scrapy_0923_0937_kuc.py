# 代码生成时间: 2025-09-23 09:37:34
import scrapy
def generate_excel(data, filename):
    """Generate an Excel file from a given data dictionary.

    Args:
        data (dict): A dictionary containing data to be written to the Excel file.
        filename (str): The name of the Excel file to be created.
    """
    try:
        import xlsxwriter
# 优化算法效率
        workbook = xlsxwriter.Workbook(filename)
# 扩展功能模块
        worksheet = workbook.add_worksheet()
        
        # Write data to Excel
        for row_num, (key, value) in enumerate(data.items(), 1):
            worksheet.write(row_num, 0, key)
            worksheet.write(row_num, 1, value)
            
        workbook.close()
        print(f"Excel file '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the Excel file: {e}")

# Example usage
if __name__ == '__main__':
    # Create a sample data dictionary
    data = {
        "Name": "John Doe",
# NOTE: 重要实现细节
        "Age": 30,
# 改进用户体验
        "Email": "john.doe@example.com"
    }
    
    # Generate an Excel file
    generate_excel(data, 'example.xlsx')
# 改进用户体验