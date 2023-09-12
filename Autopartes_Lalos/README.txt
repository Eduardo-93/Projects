---------------------------------------------------------------------------------------------------------------------
PARA UNA SOLA LINEA A PARTIR DE LA COLUMNA E2
---------------------------------------------------------------------------------------------------------------------
Sub SEPARACION()
Range("E2").Select

Dim i As Long
Dim ValC As String
Dim ValTC As String

i = 2

Do While ActiveCell.Offset(0, -2) <> ""
    
    ValC = Range("C" & i).Value
    ValTC = Range("E1").Value
    
    If (ValC = ValTC) Then
            ActiveCell.Value = ActiveCell.Offset(0, -1)
        Else
            ActiveCell.Value = ""
    End If
    
    ActiveCell.Offset(1, 0).Select
    i = i + 1
Loop

End Sub
---------------------------------------------------------------------------------------------------------------------
PARA TODAS LAS COLUMNAS A PARTIR DE LA COLUMNA E2
---------------------------------------------------------------------------------------------------------------------
Sub SEPARACION()
Range("E2").Select

Dim i As Long
Dim j As Long
Dim k As Long
Dim l As Long
Dim m As Long
Dim ValC As String
Dim ValTC As String

j = -2
k = -1
l = 0
Do While ActiveCell.Offset(-1, 0) <> ""
i = 2
l = 0
m = -1
    Do While ActiveCell.Offset(0, j) <> ""
    
        ValC = Range("C" & i).Value
        ValTC = ActiveCell.Offset(m, l).Value
        
        If (ValC = ValTC) Then
                ActiveCell.Value = ActiveCell.Offset(0, k).Value
            Else
                ActiveCell.Value = ""
        End If
        
        ActiveCell.Offset(1, 0).Select
        i = i + 1
        m = m - 1
        
    Loop
    
ActiveCell.Offset(m + 1, 1).Select
j = j - 1
k = k - 1
l = l + 1

Loop

End Sub
---------------------------------------------------------------------------------------------------------------------
PARA RELLENAR TODO CON EL INT PRINCIPAL
---------------------------------------------------------------------------------------------------------------------
Sub Relleno()
Range("I2").Select

Dim i As Long
Dim j As Long

i = -1
j = -8

Do While ActiveCell.Offset(0, i) <> ""

    If ActiveCell.Offset(0, i) = ActiveCell.Offset(1, i) & ActiveCell.Offset(0, j) = "" Then
    
            ActiveCell.Value = ActiveCell.Offset(1, j)

    ElseIf ActiveCell.Offset(0, i) = ActiveCell.Offset(1, i) Then
    
            ActiveCell.Value = ActiveCell.Offset(0, j)
            
    ElseIf ActiveCell.Offset(0, j) = "" & ActiveCell.Offset(0, i) = ActiveCell.Offset(-1, i) Then
            
            ActiveCell.Value = ActiveCell.Offset(-1, j)
            
    Else
            ActiveCell.Value = ActiveCell.Offset(0, j)
            
    End If
    
    ActiveCell.Offset(1, 0).Select
    
Loop

Range("I2").Select
Do While ActiveCell.Offset(0, i) <> ""

    If ActiveCell.Offset(0, i) <> ActiveCell.Offset(-1, i) Then
    
    ElseIf ActiveCell = "" Then
    
        ActiveCell.Value = ActiveCell.Offset(-1, 0)
            
    End If
    
    ActiveCell.Offset(1, 0).Select
    
Loop

End Sub
---------------------------------------------------------------------------------------------------------------------
