using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconName)
            {
                return iconName switch
                {
                    "Pencil" => "\uE70F", // Edit
                    "Eye" => "\uE18B",    // View
                    "Copy" => "\uE8C8",   // Copy
                    "Plus" => "\uE710",   // Add
                    "Shield" => "\uEA18", // DefenderBadge12
                    "Calendar" => "\uE787", // CalendarDay
                    "History" => "\uE81C", // History
                    _ => "\uE711" // Default (Cancel / Cross)
                };
            }
            return value;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
