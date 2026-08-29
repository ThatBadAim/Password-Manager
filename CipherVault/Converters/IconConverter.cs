using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconType)
            {
                switch (iconType)
                {
                    case "Pencil": return "\uE70F";
                    case "Eye": return "\uE18B";
                    case "Copy": return "\uE8C8";
                    case "Plus": return "\uE710";
                    default: return "\uE716"; // Default circle or dot
                }
            }
            return "\uE716";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
