def afficher_wcs_projet1():
    import streamlit as st
    from streamlit_carousel import carousel

    # Titre + expliaction projet
    st.markdown("<h1 style='text-align: center; color: white;'>Projet 1 : Analyse de données avec MySQL et Power BI</h1>", unsafe_allow_html=True)

    #Espace
    st.write("")
    st.write("")

    st.markdown("""
    <div style='text-align: center; color: white; font-size: 20px;'>
    Dans ce projet, j'ai travaillé sur l'analyse de données provenant d'une base de données MySQL 📊.  
    Le but était de requêter et manipuler les données en SQL pour en extraire des informations clés.
    </div>
    """, unsafe_allow_html=True)

    #Espace
    st.write("")
    st.write("")

    # Explication projet
    st.markdown("""
    ## 🔍 Étapes réalisées :
    """)

    #Espace
    st.write("")
    st.write("")

    st.markdown("""
    ### 1️⃣ Requête SQL 💻 :
    - Extraction des données pertinentes à l'aide de requêtes SQL.
    - Utilisation de jointures, agrégations et filtres pour répondre aux besoins spécifiques.
    """)


    # Selectbox pour afficher les requête SQL
    section = st.selectbox(" ", ["Choisissez une requête SQL",
                                "Nombre de produits vendus par catégorie et par mois sur les 2 derniéres années",
                                "Taux de variation des ventes par rapport au mois précédent",
                                "Chaque mois, les 2 vendeurs ayant réalisés le plus de chiffre d’affaires",
                                "Stock des produits et nombre de commandes + prix du d'achat",
                                "Bénéfice par pays"
                                ])
        
    if section == "Nombre de produits vendus par catégorie et par mois sur les 2 derniéres années":
            st.code("""
            SELECT 
                SUM(od.quantityOrdered) AS total_commande, 
                p.productLine, 
                p.productName, 
                YEAR(o.orderDate) AS annee, 
                MONTH(o.orderDate) AS mois,
                CONCAT(
                    YEAR(o.orderDate), "-", 
                    LPAD(MONTH(o.orderDate), 2, '0'), "-01"
                ) AS dateID
            FROM 
                products AS p
            JOIN 
                orderdetails AS od ON od.productCode = p.productCode
            JOIN 
                orders AS o ON o.orderNumber = od.orderNumber
            WHERE 
                o.orderDate >= DATE_SUB(
                    (SELECT MAX(od1.orderDate) FROM orders AS od1), INTERVAL 2 YEAR
                )
            GROUP BY 
                p.productLine, 
                p.productName, 
                annee, 
                mois, 
                dateID
            ORDER BY 
                annee, 
                mois, 
                p.productLine;
            """, language='sql')
        
    if section == "Taux de variation des ventes par rapport au mois précédent":
            st.code("""
                SELECT 
                *,
                ((sq.qt1 - sq.qt0) / sq.qt0 * 100) AS tx_var
            FROM (
                SELECT
                    YEAR(o.orderDate) AS annee,
                    MONTH(o.orderDate) AS mois,
                    p.productLine AS cat,
                    CONCAT(
                        YEAR(o.orderDate), "-", 
                        LPAD(MONTH(o.orderDate), 2, '0'), "-01"
                    ) AS dateID,
                    SUM(od.quantityOrdered) AS qt1,
                    LAG(SUM(od.quantityOrdered), 12) OVER (
                        PARTITION BY p.productLine 
                        ORDER BY YEAR(o.orderDate), MONTH(o.orderDate)
                    ) AS qt0
                FROM 
                    orderdetails od
                JOIN 
                    products p ON od.productCode = p.productCode
                JOIN 
                    orders o ON o.orderNumber = od.orderNumber
                GROUP BY
                    YEAR(o.orderDate),
                    MONTH(o.orderDate),
                    p.productLine,
                    CONCAT(YEAR(o.orderDate), "-", LPAD(MONTH(o.orderDate), 2, '0'), "-01")
            ) AS sq
            ORDER BY 
            annee, mois;
            """, language='sql')
                
    if section == "Chaque mois, les 2 vendeurs ayant réalisés le plus de chiffre d’affaires":
            st.code("""
                        SELECT 
                CONCAT(e.firstName, " ", e.lastname) AS vendeur, 
                SUM(p.amount) AS chiffresAffaireParVendeur,
                e.officeCode,
                YEAR(o.orderDate) AS annee,
                MONTH(o.orderDate) AS mois,
                CONCAT(
                    YEAR(o.orderDate), "-", 
                    LPAD(MONTH(o.orderDate), 2, '0'), "-01"
                ) AS dateID
            FROM 
                employees AS e
            JOIN 
                customers AS c ON e.employeeNumber = c.salesRepEmployeeNumber
            JOIN 
                payments AS p ON p.customerNumber = c.customerNumber
            JOIN 
                orders AS o ON c.customerNumber = o.customerNumber
            GROUP BY 
                vendeur, 
                annee, 
                mois, 
                dateID,
                e.officeCode
            ORDER BY 
                annee, 
                mois;
            """, language='sql')

    if section == "Stock des produits et nombre de commandes + prix du d'achat":
            st.code("""
                    SELECT *
            FROM (
                SELECT
                    products.productName,
                    quantityInStock,
                    SUM(quantityOrdered) AS TotalQuantityOrdered,
                    buyPrice,
                    YEAR(o.orderDate) AS annee,
                    MONTH(o.orderDate) AS mois,
                    CONCAT(YEAR(o.orderDate), "-", LPAD(MONTH(o.orderDate), 2, '0'), "-01") AS dateID
                FROM orderdetails AS od
                JOIN products ON products.productCode = od.productCode
                JOIN orders as o ON o.orderNumber=od.orderNumber
                GROUP BY products.productCode, products.productName, quantityInStock, buyPrice, annee, mois, dateID
                ORDER BY TotalQuantityOrdered
            ) AS stock;
            """, language='sql')
        
    if section == "Bénéfice par pays":
            st.code("""
                    SELECT 
            c.country, 
            (SUM(od1.priceEach * od1.quantityOrdered) - SUM(p.buyPrice)) AS beneficeParPays,
            YEAR(od.orderDate) AS annee,
            MONTH(od.orderDate) AS mois,
            CONCAT(YEAR(od.orderDate), "-", LPAD(MONTH(od.orderDate), 2, '0'), "-01") AS dateID
        FROM 
            orderdetails AS od1
        JOIN 
            orders AS od ON od1.orderNumber = od.orderNumber
        JOIN 
            customers AS c ON od.customerNumber = c.customerNumber
        JOIN 
            products AS p ON od1.productCode = p.productCode
        GROUP BY 
            c.country, annee, mois, dateID;
        """, language='sql')

    #Espace
    st.write("")
    st.write("")
            
    st.markdown("""
        ### 2️⃣ Calcul des KPI 📈 :
        - Calcul des indicateurs de performance (KPI) comme :  
        - **Chiffre d'affaires.**  
        - **Croissance des ventes.**
                """)
        
    #Espace
    st.write("")
    st.write("")

    st.markdown("""
        ### 3️⃣ Création du Dashboard Power BI 🎨 :
        - Développement d'un tableau de bord interactif pour visualiser les KPIs.
        - Utilisation de graphiques dynamiques pour faciliter la prise de décision stratégique.
        """)

        #Espace
    st.write("")
    st.write("")

    st.markdown("""
        ## 💡 Résultat :
        Un tableau de bord clair et efficace, permettant à l'entreprise de mieux comprendre ses performances et d'identifier des axes d'amélioration.
        """)

    #Espace
    st.write("")
    st.write("")

    # Carousel images power BI
    test_items = [
        dict(
            title="",
            text="",
            img="wcs/projet_1/ressources/page1.png"
            ),
        dict(
            title="",
            text="",
            img="wcs/projet_1/ressources/page2.png"
            ),
        dict(
            title="",
            text="",
            img="wcs/projet_1/ressources/page3.png"
            ),
        dict(
            title="",
            text="",
            img="wcs/projet_1/ressources/page4.png"
            ),

        ]

    carousel(items=test_items,container_height=700)
