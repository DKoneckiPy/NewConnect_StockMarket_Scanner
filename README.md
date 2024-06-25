# NewConnect_StockMarket_Scanner

Script containing two tools: getting single company data by ticker and NewConnect(Warsaw Stock Exchange market) market scanner using web scraping

First tool: user need to enter the name of the company(ticker), starting year month and day. Obtaining data with get_data_stooq

Second tool: Extracting Data with BeautifulSoup from each page (Stooq divides the company list into several parts), setting filter by daily price change (in this case D1>+20%) and drawing charts of price changes for filtered companies

Data source: https://stooq.pl/q/i/?s=ncindex




Function ConvertTableToCSV(tableText As String) As String
    Dim lines() As String
    Dim csv As String
    Dim i As Integer

    lines = Split(tableText, vbCrLf)
    
    ' Nagłówek tabeli
    csv = "Format,Stawka1,Stawka2" & vbCrLf
    
    ' Przekształć linie w wiersze tabeli
    For i = 1 To UBound(lines) Step 3
        If i + 2 <= UBound(lines) Then
            csv = csv & Trim(lines(i)) & "," & Trim(lines(i + 1)) & "," & Trim(lines(i + 2)) & vbCrLf
        End If
    Next i

    ConvertTableToCSV = csv
End Function

Sub SaveCSVToFile(csvData As String, filePath As String)
    Dim fso As Object
    Dim file As Object

    Set fso = CreateObject("Scripting.FileSystemObject")
    Set file = fso.CreateTextFile(filePath, True)
    file.Write csvData
    file.Close
End Sub
