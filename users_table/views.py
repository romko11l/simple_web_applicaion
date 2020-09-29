from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods
import sqlite3


@require_http_methods(['GET'])
def give_my_table(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT id, login FROM users WHERE status='active'")
    results = cursor.fetchall()
    conn.close()
    return render(request, 'users_table/index.html', context={'posts': results})


@require_http_methods(['GET'])
def give_my_table_by_login(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    sql_part = request.GET['login']
    cursor.execute("SELECT id, login FROM users WHERE login='" + sql_part + "'")
    results = cursor.fetchall()
    conn.close()
    return render(request, 'users_table/index.html', context={'posts': results})


@require_http_methods(['GET'])
def give_my_table_by_id(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    sql_part = request.GET['id']
    cursor.execute("SELECT id, login FROM users WHERE id='" + sql_part + "'")
    results = cursor.fetchall()
    conn.close()
    return render(request, 'users_table/index.html', context={'posts': results})
