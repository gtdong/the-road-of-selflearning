#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import models


def student_register(name, password):
    obj = models.Student.get_obj_by_name(name)
    if not obj:
        student = models.Student()
        student.register(name, password)
        return True, 'student %s register successfully' % name, student.name
    else:
        return False, 'userName exisit,please change', None


def choose_school(student_name, school_name):
    obj = models.Student.get_obj_by_name(student_name)
    if obj.school:
        return False, '你已经选过校区了'
    else:
        obj.choose_school(school_name)
        return True, '%s choose % school,success' % (student_name, school_name)


def get_school_by_student(student_name):
    obj_student = models.Student.get_obj_by_name(student_name)
    return obj_student.school


def get_can_choose_course(student_name):
    obj_student = models.Student.get_obj_by_name(student_name)
    if obj_student.school:
        obj_school = models.School.get_obj_by_name(obj_student.school)
        return True, 'success', obj_school.course_name_list
    else:
        return False, 'please choose school first', None


def choose_course(student_name, course_name):
    obj_student = models.Student.get_obj_by_name(student_name)
    obj_course = models.Course.get_obj_by_name(course_name)
    obj_student.choose_course(course_name)
    obj_course.add_student(student_name)

    return True, '%s choose %s course,success' % (student_name, course_name)


def get_score(student_name):
    obj_student = models.Student.get_obj_by_name(student_name)
    return obj_student.scores
