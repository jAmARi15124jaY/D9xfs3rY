# 代码生成时间: 2025-09-24 13:45:11
import scrapy
def generate_chart(data):
    """
    生成交互式图表的函数。
    
    参数:
    data (dict): 包含图表数据的字典。
    """
    try:
        # 导入图表库
        from bokeh.plotting import figure, show, output_file
        from bokeh.models import ColumnDataSource
        
        # 检查数据是否有效
        if not data or 'x' not in data or 'y' not in data:
            raise ValueError("Data must contain 'x' and 'y' keys.")
        
        # 创建数据源
        source = ColumnDataSource(data)
        
        # 创建图表
        p = figure(title='Interactive Chart', x_axis_label='X', y_axis_label='Y')
        p.line(x='x', y='y', source=source)
        
        # 输出图表文件
        output_file('chart.html')
        show(p)
    except ImportError:
        print("Bokeh library is required to generate charts.")
    except ValueError as e:
        print(f"Error: {e}")
def main():
    """
    主函数，用于运行图表生成器。
    """
    # 示例数据
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 5, 8, 2, 7]
    }
    
    # 生成图表
    generate_chart(data)

if __name__ == '__main__':
    main()