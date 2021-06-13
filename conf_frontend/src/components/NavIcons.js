const NavIcons = () => {
    return (
        <div className="navigation-icons">
        <a href="https://instagram.com/mimoudix" className="navigation-link">
          <i className="far fa-compass"></i>
        </a>
        <a className="navigation-link notifica">
          <i className="far fa-heart">
            <div className="notification-bubble-wrapper">
              <div className="notification-bubble">
                <span className="notifications-count">99</span>
              </div>
            </div>
          </i>
        </a>
        <a href="https://instagram.com/mimoudix" className="navigation-link">
          <i className="far fa-user-circle"></i>
        </a>      
      </div>
    )
}

export default NavIcons
