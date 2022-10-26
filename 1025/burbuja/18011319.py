#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Nombre: Salvador Serna Ramirez
# No. Control: 18011319
# Calificación: XXX

x = [90, 55, 10, 72, 69, 34]

num = len(x)
i = 0
while i < num:
      j = i
      while j < num:
              if x[i] > x[j]:
                      aux = x[i]
                      x[i] = x[j]
                      x[j] = aux
              j = j + 1
      i = i + 1

print("Lista ordenada: ")
print(x)