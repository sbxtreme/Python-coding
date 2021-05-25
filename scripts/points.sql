SELECT
DISTINCT
  (userid) as user_id,
  -- the below query is for award_points point account
  (SELECT
    ISNULL((SELECT
      upa1.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa1 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa1 (NOLOCK)
      ON upa1.PointAccountID = pa1.id
      AND upa1.userid = upa.userid
    WHERE upa1.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa1.id = '36E09356-7EA5-4C3F-95CD-8EDCB7BD60C6'), 0))
  AS award_points,

  -- the below query is for ay_lifetime_tier_points point account
  (SELECT
    ISNULL((SELECT
      upa2.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa2 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa2 (NOLOCK)
      ON upa2.PointAccountID = pa2.id
      AND upa2.userid = upa.userid
    WHERE upa2.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa2.id = '5B2A77BE-35DC-46DF-9C42-C3EA9DE7E563'), 0))
  AS ay_lifetime_tier_points,

  -- the below query is for ay_qualifying_flights point account
  (SELECT
    ISNULL((SELECT
      upa3.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa3 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa3 (NOLOCK)
      ON upa3.PointAccountID = pa3.id
      AND upa3.userid = upa.userid
    WHERE upa3.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa3.id = '432BC55B-2A2E-474C-B891-DBB572B7F2A1'), 0))
  AS ay_qualifying_flights,

  -- the below query is for ay_qualifying_revenue point account
  (SELECT
    ISNULL((SELECT
      upa4.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa4 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa4 (NOLOCK)
      ON upa4.PointAccountID = pa4.id
      AND upa4.userid = upa.userid
    WHERE upa4.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa4.id = 'BFEC4F7E-C985-4A6F-B626-230B085B0BCE'), 0))
  AS ay_qualifying_revenue,

  -- the below query is for ay_tier_qualifying_points point account
  (SELECT
    ISNULL((SELECT
      upa5.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa5 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa5 (NOLOCK)
      ON upa5.PointAccountID = pa5.id
      AND upa5.userid = upa.userid
    WHERE upa5.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa5.id = '2C0A913A-9E41-4A89-AB2F-E60196AA11D1'), 0))
  AS ay_tier_qualifying_points,

  -- the below query is for gold_tier_counter point account
  (SELECT
    ISNULL((SELECT
      upa6.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa6 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa6 (NOLOCK)
      ON upa6.PointAccountID = pa6.id
      AND upa6.userid = upa.userid
    WHERE upa6.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa6.id = '2E170433-2618-481E-979E-03B51EBE93DE'), 0))
  AS gold_tier_counter,

  -- the below query is for platinum_tier_counter point account
  (SELECT
    ISNULL((SELECT
      upa7.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa7 (NOLOCK) 
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa7 (NOLOCK)
      ON upa7.PointAccountID = pa7.id
      AND upa7.userid = upa.userid
    WHERE upa7.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa7.id = 'F185F5B9-75FD-46C5-AF06-7B8D2A74C881'), 0))
  AS platinum_tier_counter,

  -- the below query is for qualifying_flights point account
  (SELECT
    ISNULL((SELECT
      upa8.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa8 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa8 (NOLOCK)
      ON upa8.PointAccountID = pa8.id
      AND upa8.userid = upa.userid
    WHERE upa8.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa8.id = 'FFE1D688-B669-479A-828C-7738C8D9F155'), 0))
  AS qualifying_flights,

  -- the below query is for silver_tier_counter point account
  (SELECT
    ISNULL((SELECT
      upa9.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa9 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa9 (NOLOCK)
      ON upa9.PointAccountID = pa9.id
      AND upa9.userid = upa.userid
    WHERE upa9.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa9.id = '6B0CD5D7-944D-4301-B0CA-06024160F168'), 0))
  AS silver_tier_counter,

  -- the below query is for tier_qualifying_points point account
  (SELECT
    ISNULL((SELECT
      upa11.availablebalance
    FROM [finnair-incentives].incent.PointAccounts pa11 (NOLOCK)
    INNER JOIN [finnair-incentives].incent.UserPointAccounts upa11 (NOLOCK)
      ON upa11.PointAccountID = pa11.id
      AND upa11.userid = upa.userid
    WHERE upa11.retailerid = (SELECT
      id
    FROM retailers (NOLOCK)
    WHERE name = 'finnair')
    AND active = 'true'
    AND pa11.id = 'C3FAFF23-F636-44FD-8A05-D885BDD4C803'), 0))
  AS tier_qualifying_points

FROM [finnair-incentives].incent.UserPointAccounts upa (NOLOCK)
WHERE upa.retailerid = (SELECT
  id
FROM retailers (NOLOCK)
WHERE name = 'finnair')
-- below is used for passing userid list
AND userid in ({})