from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse
from datetime import datetime  

# Create your views here.

def welcome(response):
    content= "<html><head><title>Welcome to Django</title></head>"
    content += "<body style='color:white;background-color:orange;'>"
    content += "<center>"
    content += "<h1>Welcome to DJANGO Programming</h1>"
    content += "<h2>Table And Some Random Data</h2>"
    content += "<table border='1' bordercolor='white'style='font-size:25px;vertical-align:bottom;' height='250' width='700' cellspacing='5' cellpadding='10'><tr><th>Name</th><th>Age</th><th>Salary</th></tr>"
    content += "<tr><td>Alby</td><td>20</td><td>12000</td></tr>"
    content += "<tr><td>Ronal</td><td>21</td><td>17000</td></tr>"
    content += "<tr><td>Leeya</td><td>20</td><td>15000</td></tr>"
    content += "<tr><td>Abin</td><td>20</td><td>18000</td></tr></table>"
    content += "</center></body></html>"
    return HttpResponse(content)

def greetings(response):
    dt=datetime.now().date()
    tm=datetime.now().time()
    msg="<html><head><title>Greetings </title></head></html>"
    msg +="<body bgcolor='pink' text='blue'>"
    msg +="<center>"
    msg+="<h1> Welcome to Django Web Development</h1>"
    msg+="<h2>Date:"+ str(dt)+"</h2>"
    msg+="<h2>Time:"+ str(tm)+"</h2>"
    msg+="</center></body></html>"
    return HttpResponse(msg)

def wishing(response):
    dt=datetime.now().date()
    tm=datetime.now().time()
    hr=tm.hour #getting hour of time
    if hr >= 6 and hr < 12: #6 Am-12 PM
        greetings="Good Morning"
    elif hr >= 12 and hr < 16: #12 PM-4 PM
        greetings="Good Afternoon"
    elif hr >= 16 and hr < 23: #4pm -11 pm
        greetings="Good Evening"
    else: #after 11PM to 6AM
        greetings="Go to sleep, Good Night"
    msg ="<html><body bgcolor='yellow' text='green'>"
    msg +="<center>"
    msg+="<h1> Welcome to Django Web Development</h1>"
    msg+="<h2>Date:"+ str(dt)+"</h2>"
    msg+="<h2>Time:"+ str(tm)+"</h2>"
    msg+="<h2>" + greetings +"</h2>"
    msg+="</center></body></html>"
    return HttpResponse(msg)

def calculator(request):
    """A simple calculator view"""
    result = ''
    if request.method == 'GET':
        num1 = request.GET.get('num1', '')
        num2 = request.GET.get('num2', '')
        operation = request.GET.get('operation', '')
        
        if num1 and num2 and operation:
            num1, num2 = float(num1), float(num2)
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'

    msg = f"""
    <html>
    <head><title>Calculator</title></head>
    <body bgcolor='lightblue' text='darkblue'>
    <center>
    <h1>Simple Calculator</h1>
    <form>
        <input type='number' name='num1' placeholder='First Number' step='any'>
        <select name='operation'>
            <option value='add'>+</option>
            <option value='subtract'>-</option>
            <option value='multiply'>×</option>
            <option value='divide'>÷</option>
        </select>
        <input type='number' name='num2' placeholder='Second Number' step='any'>
        <input type='submit' value='Calculate'>
    </form>
    <h2>Result: {result}</h2>
    </center>
    </body>
    </html>
    """
    return HttpResponse(msg)

def todo_list(request):
    """A simple todo list with localStorage"""
    msg = """
    <html>
    <head>
        <title>Todo List</title>
        <style>
            .todo-item { margin: 10px; padding: 10px; background: #f0f0f0; }
            .done { text-decoration: line-through; background: #e0e0e0; }
        </style>
    </head>
    <body bgcolor='mintcream' text='darkgreen'>
    <center>
        <h1>Todo List</h1>
        <input type='text' id='newTodo' placeholder='Add new task'>
        <button onclick='addTodo()'>Add</button>
        <div id='todoList'></div>
    </center>
    <script>
        let todos = JSON.parse(localStorage.getItem('todos') || '[]');
        
        function renderTodos() {
            const list = document.getElementById('todoList');
            list.innerHTML = todos.map((todo, index) => `
                <div class='todo-item ${todo.done ? "done" : ""}'>
                    <input type='checkbox' ${todo.done ? "checked" : ""} 
                           onclick='toggleTodo(${index})'>
                    ${todo.text}
                    <button onclick='deleteTodo(${index})'>Delete</button>
                </div>
            `).join('');
            localStorage.setItem('todos', JSON.stringify(todos));
        }
        
        function addTodo() {
            const input = document.getElementById('newTodo');
            if(input.value.trim()) {
                todos.push({text: input.value, done: false});
                input.value = '';
                renderTodos();
            }
        }
        
        function toggleTodo(index) {
            todos[index].done = !todos[index].done;
            renderTodos();
        }
        
        function deleteTodo(index) {
            todos.splice(index, 1);
            renderTodos();
        }
        
        renderTodos();
    </script>
    </body>
    </html>
    """
    return HttpResponse(msg)

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        Employee.objects.create(
            emp_name=request.POST['emp_name'],
            salary=request.POST['salary'],
            department=request.POST['department'],
            designation=request.POST['designation']
        )
        return redirect('employee_list')
    return render(request, 'employee_form.html')

def employee_edit(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    if request.method == 'POST':
        employee.emp_name = request.POST['emp_name']
        employee.salary = request.POST['salary']
        employee.department = request.POST['department']
        employee.designation = request.POST['designation']
        employee.save()
        return redirect('employee_list')
    return render(request, 'employee_form.html', {'employee': employee})

def employee_delete(request, emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    employee.delete()
    return redirect('employee_list')
