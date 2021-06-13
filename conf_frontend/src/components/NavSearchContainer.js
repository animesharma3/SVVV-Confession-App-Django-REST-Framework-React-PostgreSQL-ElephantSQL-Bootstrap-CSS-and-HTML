const NavSearchContainer = () => {
    return (
        <div className="navigation-search-container">
            <i className="fa fa-search"></i>
            <input className="search-field" type="text" placeholder="Search"></input>
            <div className="search-container">
                <div className="search-container-box">
                    <div className="search-results">

                    </div>
                </div>
            </div>
        </div>
    )
}

export default NavSearchContainer
