import csv

with open('new_vgsale.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    row1 = csv.reader(csvfile)
    rows = csv.DictReader(csvfile)

    # 以迴圈輸出每一列
    # for row in rows:
    # print(row['platform_n'], ".", row['Platform'])
    with open('new_vgsale2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['num', 'Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales',
                         'JP_Sales', 'Other_Sales', 'Global_Sales', 'genre_n', 'publisher_n', 'platform_n', 'adjPlatform', 'adjGenre'])
        for row in rows:
            writer.writerow(
                [row['num'], row['Rank'], row['Name'], row['Platform'], row['Year'], row['Genre'], row['Publisher'], row['NA_Sales'], row['EU_Sales'], row['JP_Sales'], row['Other_Sales'], row['Global_Sales'], row['genre_n'], row['publisher_n'], row['platform_n'], row['platform_n'] + "."+row['Platform'], row['genre_n'] + "."+row['Genre']])
