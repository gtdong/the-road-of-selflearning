#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import models
from lib import common
from conf import settings
import os


def check_course(teacher_name):
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    course_list = teacher_obj.get_teach_course()
    return course_list


def check_all_course():
    base_dir_course = os.path.join(settings.BASE_DB, 'course')
    course_list = common.get_all_file(base_dir_course)
    return course_list
def choose_course(teacher_name,course_name):
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    teacher_obj.bind_to_course(course_name)

def check_student_by_course(course_name):
    '''
    查看课程下所有的学生
    :param course_name:
    :return:
    '''
    course_obj = models.Course.get_obj_by_name(course_name)
    return course_obj.student_name_list
def change_student_scour(teacher_name,student_name,course_name,score):
    teacher_obj = models.Teacher.get_obj_by_name(teacher_name)
    student_obj = models.Student.get_obj_by_name(student_name)
    teacher_obj.change_student_score(student_obj,course_name,score)
