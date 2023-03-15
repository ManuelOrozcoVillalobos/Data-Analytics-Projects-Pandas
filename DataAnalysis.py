import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution


if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
            'B_office_data.xml' not in os.listdir('../Data') and
            'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

    # All data in now loaded to the Data folder.
    df_a = pd.read_xml('../Data/A_office_data.xml')
    df_b = pd.read_xml('../Data/B_office_data.xml')
    df_hr = pd.read_xml('../Data/hr_data.xml')
    df_a.index = [f'A{num}' for num in df_a['employee_office_id']]
    df_b.index = [f'B{num}' for num in df_b['employee_office_id']]
    df_hr.set_index('employee_id', inplace=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    df_office = pd.concat([df_a, df_b])

    office_hr = df_office.merge(df_hr, left_index=True, right_index=True, indicator=True)
    office_hr.sort_index(inplace=True)
    office_hr.drop(columns=['employee_office_id', '_merge'], inplace=True)

    controller = 1
    departments_list = ['sales', 'technical', 'support', 'IT', 'product_mng',
                        'RandD', 'marketing', 'management', 'hr', 'accounting']

    while controller != 0:
        try:
            controller = int(input('Visualization Menu:\n'
                                   'Choose your option to visualize\n'
                                   '    1.Top employees by department\n'
                                   '    2.Number of projects worked by low paid employees\n'
                                   '    3.Evaluation of productivity and satisfaction of employees\n'
                                   '    Exit the app\n'
                                   ''))

            if controller == 1:
                employee_quant = int(input('Select the number of top employees you want to display:\n'))
                top_departments = office_hr.sort_values(by='Department').nlargest(employee_quant, 'average_monthly_hours')[['Department', 'average_monthly_hours']]
                print(f"The top {employee_quant} departments are:\n"
                      f"{top_departments}\n")

            if controller == 2:
                department = input("Enter the department from which you want to know the project hours:\n")
                if department in departments_list:
                    projects_number = sum(office_hr.query("salary == 'low' & Department == 'IT'")['number_project'])
                    print(f"The number of projects worked for low paid employees in this department is:\n "
                          f"{projects_number}\n")
                else:
                    print('Please select a department that belongs to our company\n')

            if controller == 3:
                try:
                    employees = input('Input the employees to evaluate separated by a comma(A, B, C, ...):\n').split(",")
                    evaluation_score = office_hr.loc[employees, ['last_evaluation', 'satisfaction_level']]
                    print(f"The evaluated employee ratings are:\n"
                          f"{evaluation_score}\n")
                except KeyError:
                    print('Some of the employees you input do not exist in our database\n')

            elif controller == 0:
                print('Thank you for using our Visualization Menu')

        except ValueError:
            print('You have to select a supported integer\n')

