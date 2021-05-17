#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/12 18:22
# @Author : russell
# @File :  models
import fabric

from . import db

user_role_table = db.Table('fb_user_role',
                           db.Column(
                               'user_id',
                               db.Integer,
                               db.ForeignKey('upms_users.id')
                           ),
                           db.Column(
                               'role_id',
                               db.Integer,
                               db.ForeignKey('upms_roles.id')
                           )
                           )

role_ability_table = db.Table('fb_role_ability',
                              db.Column(
                                  'role.id',
                                  db.Integer,
                                  db.ForeignKey('upms_roles.id')
                              ),
                              db.Column(
                                  'ability_id',
                                  db.Integer,
                                  db.ForeignKey('upms_ability.id')
                              )
                              )


class User(db.Model):
    __tablename__ = "upms_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)

    role = db.relationship(
        'Role',
        secondary=user_role_table,
        back_populates='user'  # relationship 字段
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id} {self.name} {self.role}>'

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_like_name(name):
        return User.query.filter(User.name.like(f'%{name}%'))


    @staticmethod
    def get_by_id(id:str):
        return User.query.filter_by(id=id).first()

    @classmethod
    def all(cls):
        return User.query.all()

    @classmethod
    def count(cls) -> int:
        return User.query.count()

    # role
    def add_roles(self, *roles):
        for role in roles:
            self.role.append(role)

    def remove_roles(self, *roles):
        for role in roles:
            self.role.remove(role)

    def clear_roles(self):
        all = self.role.filter()
        self.remove_roles(*all)

    def reset_roles(self, *roles):
        self.clear_roles()
        self.add_roles(*roles)


class Role(db.Model):
    __tablename__ = "upms_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)

    ability = db.relationship(
        'Ability',
        secondary=role_ability_table,
        back_populates='role'  # relationship 字段
    )

    user = db.relationship(
        'User',
        secondary=user_role_table,
        back_populates='role'  # relationship 字段
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Role {self.id} {self.name} {self.ability}>'

    def __str__(self):
        return self.name

    # Role
    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def get_like_name(name):
        return Role.query.filter(Role.name.like(f'%{name}%'))



    @staticmethod
    def get_by_id(id):
        return Role.query.filter_by(id=id).first()

    @classmethod
    def all(cls):
        return Role.query.all()

    @classmethod
    def count(cls) -> int:
        return Role.query.count()

    # ability

    def add_abilities(self, *abilities):
        for ability in abilities:
            self.ability.append(ability)

    def remove_abilities(self, *abilities):
        for ability in abilities:
            self.ability.remove(ability)

    def clear_abilities(self):
        all = self.ability.filter()
        self.remove_abilities(*all)

    def reset_abilities(self, *abilities):
        self.clear_abilities()
        self.add_abilities(*abilities)


class Ability(db.Model):
    __tablename__ = "upms_ability"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True, nullable=True)  #

    role = db.relationship(
        'Role',
        secondary=role_ability_table,
        back_populates='ability'  # relationship 字段
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Ability {self.name}>'

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_name(name):
        return Ability.query.filter_by(name=name).first()

    @staticmethod
    def get_like_name(name):
        return Ability.query.filter(Ability.name.like(f'%{name}%'))




    @staticmethod
    def get_by_id(id):
        return Ability.query.filter_by(id=id).first()

    @classmethod
    def all(cls):
        return Ability.query.all()

    @classmethod
    def count(cls) -> int:
        return Ability.query.count()
