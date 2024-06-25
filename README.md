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
    
    ' Przekształć linie w wiersze tabeli, ignorując puste linie
    Dim currentRow As String
    For i = 0 To UBound(lines)
        If Trim(lines(i)) <> "" Then
            If currentRow = "" Then
                currentRow = Trim(lines(i))
            Else
                currentRow = currentRow & "," & Trim(lines(i))
                If InStr(currentRow, ",") = 2 Then ' Jeżeli currentRow zawiera 3 wartości
                    csv = csv & currentRow & vbCrLf
                    currentRow = ""
                End If
            End If
        End If
    Next i

    ConvertTableToCSV = csv
End Function
