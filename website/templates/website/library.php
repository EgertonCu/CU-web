<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eLibrary</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #288c42;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }

        .container {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .book {
            display: flex;
            align-items: center;
            background: #fff;
            margin-bottom: 1rem;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .book-icon {
            font-size: 3rem;
            color: #288c42;
            margin-right: 1rem;
        }

        .book-details {
            flex-grow: 1;
        }
        
        a { color: inherit; } 


        .book-title {
            font-size: 1.25rem;
            font-weight: bold;
            margin: 0;
        }

        .book-category {
            font-size: 0.9rem;
            color: #666;
        }

        footer {
            background-color: #288c42;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>

<!-- Include fetch file -->
<?php include 'helpers/fetch.php';?>

<body>
    <header>
        <h1>eLibrary</h1>
    </header>

    <div class="container">
        <!-- <div class="book">
            <div class="book-icon">📘</div>
            <div class="book-details">
                <p class="book-title">Book Title 1</p>
                <p class="book-category">Category: Fiction</p>
            </div>
        </div> -->

        <!-- Dynamically list books -->
        <?php listBooks();?>

        <!-- <div class="book">
            <div class="book-icon">📙</div>
            <div class="book-details">
                <p class="book-title">Book Title 3</p>
                <p class="book-category">Category: History</p>
            </div>
        </div> -->
    </div>

    <footer>
        <p>&copy; 2024 eLibrary. All rights reserved.</p>
    </footer>
</body>
</html>
