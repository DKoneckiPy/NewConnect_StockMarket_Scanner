# NewConnect_StockMarket_Scanner

Script containing two tools: getting single company data by ticker and NewConnect(Warsaw Stock Exchange market) market scanner using web scraping

First tool: user need to enter the name of the company(ticker), starting year month and day. Obtaining data with get_data_stooq

Second tool: Extracting Data with BeautifulSoup from each page (Stooq divides the company list into several parts), setting filter by daily price change (in this case D1>+20%) and drawing charts of price changes for filtered companies

Data source: https://stooq.pl/q/i/?s=ncindex


Function ConvertTableToCSV(tableText As String) As String
    Dim lines() As String
    Dim csv As String
    Dim i As Integer
    Dim lineCount As Integer

    lines = Split(tableText, vbCrLf)
    
    ' Nagłówek tabeli
    csv = "Format,Stawka1,Stawka2" & vbCrLf
    
    ' Przekształć linie w wiersze tabeli, ignorując puste linie
    lineCount = 0
    For i = 0 To UBound(lines)
        If Trim(lines(i)) <> "" Then
            If lineCount Mod 3 = 0 Then
                If lineCount > 0 Then
                    csv = csv & vbCrLf
                End If
                csv = csv & Trim(lines(i))
            Else
                csv = csv & "," & Trim(lines(i))
            End If
            lineCount = lineCount + 1
        End If
    Next i

    ConvertTableToCSV = csv
End Function


      
