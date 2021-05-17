#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 13:35
# @Author : russell
# @File :  permission


from functools import wraps
# from flask_login import current_user
from werkzeug.exceptions import Forbidden

from upms.models.permission import User, Ability, Role



# todo 获取当前账户
def import_user() -> User:
    pass
    # return User.get_by_id(1)


def user_has_ability(ability_name: str, get_user=import_user):
    def wrapper(func):
        @wraps(func)
        def innner(*args, **kwargs):
            check_ability = Ability.get_by_name(name=ability_name)
            user = get_user()
            user_abilities = set()
            for role in user.role:
                for ab in role.ability:
                    user_abilities.add(ab)

            if check_ability in user_abilities:
                return func(*args, **kwargs)
            else:
                raise Forbidden(f"1 not {ability_name}")

        return innner

    return wrapper


def user_is_role(role_name: str, get_user=import_user):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            user = get_user()
            check_role = Role.get_by_name(name=role_name)
            if check_role in user.role:
                return func(*args, **kwargs)
            raise Forbidden(f"1 not {role_name}")

        return inner

    return wrapper

# todo 黑名单,白名单















